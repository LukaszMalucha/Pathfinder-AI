$('.dropdown-trigger').dropdown();


$(".alert-user").delay(3000).fadeOut(200, function() {
    $(this).alert('close');
});

$('.card-grid').hide();
$('.img-grid').show();

$(document).ready(function() {
    $('.sidenav').sidenav();


//    Create environment

    $("#formEnvironment").on('submit', function(event) {
        $('#row-grid').empty()
        $.ajax({
            data: {
                start_location: $('#start_location').val(),
                base_location: $('#base_location').val(),
                astronauts: $('#astronauts').val(),
                desert_storm_1: $('#desert_storm_1').val(),
                desert_storm_2: $('#desert_storm_2').val(),
                desert_storm_3: $('#desert_storm_3').val(),
                desert_storm_4: $('#desert_storm_4').val(),
            },
            type : 'POST',
            url: '/environment',





        })
        .done(function(data) {

            if(data.error) {
                $('#messageAlert').text(data.error).show().fadeOut(5000);
                $('#buttonCompute').hide();
                $('.img-grid').show();
            }

            else {
                $('#buttonCompute').show();
                $('.card-grid').show();
                $('.img-grid').hide();
                for (var i = 0; i < 64; i++){
                    if (i == data.astronauts)
                      $('#row-grid').append('<div class="col-125 plain-element"><img src="/static/img/mars_astronauts.png" class="tile"></div>')
                    else if (i == data.start_location)
                       $('#row-grid').append('<div class="col-125 plain-element"><img src="/static/img/mars_buggy.png" class="tile"></div>')
                    else if (i == data.base_location)
                       $('#row-grid').append('<div class="col-125 plain-element"><img src="/static/img/mars_base.png" class="tile"></div>')
                    else if (i == data.desert_storm_1 || i == data.desert_storm_2 || i == data.desert_storm_3 || i == data.desert_storm_4)
                       $('#row-grid').append('<div class="col-125 plain-element"><img src="/static/img/mars_storm.png" class="tile"></div>')
                    else
                        $('#row-grid').append('<div class="col-125 plain-element"><div class="tile-box"></div></div>')
                }
             }
        });

        event.preventDefault();

    });

//    Compute Path

    $("#formPathfinder").on('submit', function(event) {
        $('#row-grid').empty()
        $('.card-grid').hide()
        $('.loader').show();
        $.ajax({
            type : 'POST',
            url: '/pathfinder',
        })
        .done(function(data) {
            $('.loader').hide();
            if(data.error) {
                $('#messageAlert').text(data.error).show().fadeOut(5000)
            }

            else {
                $('#buttonCompute').prop('disabled', false);
                $('.card-grid').show();
                $('.img-grid').hide();
                var path = data.path
                for (var i = 0; i < 64; i++){
                    if (i == data.astronauts)
                      $('#row-grid').append('<div class="col-125 plain-element"><img src="/static/img/mars_collection.png" class="tile"></div>')
                    else if (i == data.start_location)
                       $('#row-grid').append('<div class="col-125 plain-element"><img src="/static/img/mars_buggy.png" class="tile"></div>')
                    else if (i == data.base_location)
                       $('#row-grid').append('<div class="col-125 plain-element"><img src="/static/img/mars_base.png" class="tile"></div>')
                    else if (i == data.desert_storm_1 || i == data.desert_storm_2 || i == data.desert_storm_3 || i == data.desert_storm_4)
                       $('#row-grid').append('<div class="col-125 plain-element"><img src="/static/img/mars_storm.png" class="tile"></div>')
                    else if (data.path.includes(i.toString()))
                        $('#row-grid').append('<div class="col-125 plain-element"><img src="/static/img/mars_path.png" class="tile"></div>')
                    else
                        $('#row-grid').append('<div class="col-125 plain-element"><div class="tile-box"></div></div>')
                }
             }
        });

        event.preventDefault();

    })



});
