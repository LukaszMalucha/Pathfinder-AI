

Survey
    .StylesManager
    .applyTheme("default");
    $('#algorithm_results').hide();

var json = {
    title: "Create Planet Environment",
    showProgressBar: "bottom",
    pages: [
        {
            questions: [
                {
                    type: "text",
                    name: "start_location",
                    title: "Pathfinder Location",
                    titleLocation: "left",
                    isRequired: true,
                    validators: [
                         {
                            type: "numeric",
                            minValue: 0,
                            maxValue: 63
                        }
                    ]
                },
                {
                    type: "text",
                    name: "base_location",
                    title: "Mars Base Location",
                    titleLocation: "left",
                    isRequired: true,
                    validators: [
                         {
                            type: "numeric",
                            minValue: 0,
                            maxValue: 63
                        }
                    ]
                },
                {
                    type: "text",
                    name: "astronauts",
                    title: "Astronauts Outpost",
                    titleLocation: "left",
                    isRequired: true,
                    validators: [
                         {
                            type: "numeric",
                            minValue: 0,
                            maxValue: 63
                        }
                    ]
                },

            ]
        },
        {
        questions: [
        {
                    type: "text",
                    name: "desert_storm_1",
                    title: "Magnetic Storm #1",
                    titleLocation: "left",
                    isRequired: true,
                    validators: [
                         {
                            type: "numeric",
                            minValue: 0,
                            maxValue: 63
                        }
                    ]
                },
                {
                    type: "text",
                    name: "desert_storm_2",
                    title: "Magnetic Storm #2",
                    titleLocation: "left",
                    isRequired: true,
                    validators: [
                         {
                            type: "numeric",
                            minValue: 0,
                            maxValue: 63
                        }
                    ]
                },
                {
                    type: "text",
                    name: "desert_storm_3",
                    title: "Magnetic Storm #3",
                    titleLocation: "left",
                    isRequired: true,
                    validators: [
                         {
                            type: "numeric",
                            minValue: 0,
                            maxValue: 63
                        }
                    ]
                },


        ]
        }

    ]
};

window.survey = new Survey.Model(json);
survey.requiredText = ":"; survey.render();
Survey.surveyStrings.progressText = "Element {0} of {1}";
survey
    .onComplete

    .add(function (result) {
            $.ajax({
                dataType: 'json',
                contentType: 'application/json',
                type : 'POST',
                url : '/results',
                data : JSON.stringify(result.data),

            })

            .done(function(data) {
                 $('#algorithm_results').show();
                 $('#results').text(data.result).show();
            });

    });


$("#surveyElement").Survey({model: survey});

function animate(animitionType, duration) {
    if (!duration)
        duration = 400;
    var element = document.getElementById("surveyElement");
    $(element).velocity(animitionType, {duration: duration});
}

var doAnimantion = true;
survey.showQuestionNumbers = "off";
survey
    .onCurrentPageChanging
    .add(function (sender, options) {
        if (!doAnimantion)
            return;
        options.allowChanging = false;
        setTimeout(function () {
            doAnimantion = false;
            sender.currentPage = options.newCurrentPage;
            doAnimantion = true;
        }, 400);
        animate("fadeOut", 400);
    });
survey
    .onCurrentPageChanged
    .add(function (sender) {
        animate("fadeIn", 400);
    });
survey
    .onCompleting
    .add(function (sender, options) {
        if (!doAnimantion)
            return;
        options.allowComplete = false;
        setTimeout(function () {
            doAnimantion = false;
            sender.doComplete();
            doAnimantion = true;
        }, 400);
        animate("fadeOut", 400);
    });
animate("fadeIn", 400);
