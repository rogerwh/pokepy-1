jQuery(document).ready(function(){
    let return_url = $("#return_url").val();
    let WEBSOCKET_URI = $("#WEBSOCKET_URI").val();
    let facility = $("#facility").val();
    let div_jobstatic = '<div class="jobstatic-panel text-center" >'+
                            '<p><i class="far fa-hourglass"></i> Un momento por favor procesando tarea.</p>'+
                            '<h5 class="jobstatic-result">Si este mensaje no se actualiza en 2 minutos favor de reportarlo.</h5>'+
                        '</div>';

    let div_error = "<div id='task_error_result' class='alert alert-danger' role='alert'>"+
                        "<h4 id='title_error_result' class='alert-heading'>Error Procesando Tarea</Tarea></h4>"+
                        "<hr>"+
                        "<p id='p_error_result'></p>"+
                        "<hr>"+
                        "<p id='extra_error_resutl' class='mb-0'></p>"+
                    "</div>";

    $(".loader-position").after(div_jobstatic);

    let jobstatic_panel = $(".jobstatic-panel");
    let jobstatic_result = $(".jobstatic-result");
    let loading_gif = $(".loading-gif");

    var ws4redis = WS4Redis({
        uri: WEBSOCKET_URI+facility,
        connecting: on_connecting,
        connected: on_connected,
        receive_message: receiveMessage,
        disconnected: on_disconnected,
    });

    function on_connecting() {
        console.log('Websocket is connecting...');
    }

    function on_connected() {
        ws4redis.send_message('Hello');
    }

    function on_disconnected(evt) {
        console.log('Websocket was disconnected: ' + JSON.stringify(evt));
    }

    function receiveMessage(msg) {
        let data = JSON.parse(msg);
        let status = data.status;

        if(status === "PROGRESS"){
            data.hideLoader         ? loading_gif.hide()        : loading_gif.show();
            data.hideLoader         ? jobstatic_panel.hide()    : jobstatic_panel.show();
            data.executeFunction    ? task_function(data)       : null;
            
            //loading_gif.show();
            //jobstatic_panel.show();
            task_progress(data);
            

        }else if ( status  === "DONE") {
            ws4redis.close();
            if(typeof task_custom_done == 'function'){
                task_custom_done(data)
            }else{
                task_default_done(data)
            }

        }

        if (status === "ERROR"){
            ws4redis.close();
            taks_error(data)

        }

    }

    function task_progress(data){
        jobstatic_result.empty().append(data.mensaje);
    }
    
    function task_default_done() {
        //debugger;
        if(return_url !== null || return_url !== ""){
            window.location.replace(return_url)
        }
        loading_gif.hide();
        jobstatic_panel.hide();

    }

    function taks_error(data) {
        loading_gif.hide();
        jobstatic_panel.hide();
        let mostrar_task_id = true;
        if(typeof(data.ocultar_task_id) != 'undefined'){
            mostrar_task_id = false
        }
        $(".page-title-box").after(div_error);
        //$("#title_error_result").html(data.mensaje);
        $("#p_error_result").html(data.mensaje);
        if (mostrar_task_id) {
            $("#extra_error_resutl").html("Puede reportarlo por chat con el siguiente codigo: <strong>\
            " + data.task_id + "</strong>")
        }


    }
});