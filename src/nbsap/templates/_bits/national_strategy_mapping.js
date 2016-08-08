$(".chzn-select").chosen();
$(function () {

  forbidCrossChoicesIntersection('aichi_target', 'other_targets');

  showObjectiveCodeValue('nat_objective',
                         '.objective_text',
                         "{% url 'objective_title' pk=1 %}");

  showTargetCodeValue('aichi_targets',
                  '.target_text',
                  "{% url 'aichi_target_title' pk=1 %}");

  showTargetCodeValue('other_targets',
                      '.other_target_text',
                      "{% url 'aichi_target_title' pk=1 %}");

  showActionCodeValue('eu_actions',
                      '.actions_text',
                      "{% url 'action_title' pk=1 %}");

  $('select[name=aichi_goals]').on('change', function () {
    var option = $(this).val();
    var text = $(this).parents('.form-group').find('.goal_text');
    if (option == null){
      $(this).val = '';
      text.html('');
    } else {
      var urls = [];
      $.each(option, function(i, op){
        url = "{% url 'goal_title' pk=1%}".replace('1', op);
        urls.push(url);
      });

      $.each(urls, function(i, url){
        text.html('');
        $.get(url, function (data) {
          data = $.parseJSON(data)[0];

          text.append('<h5>Goal ' + data.code.toUpperCase() + '</h5>');
          text.append('<p>' + data.goal + '</p>');
          $('select[name=aichi_targets]').html('');
          $.each(data.targets, function(i,t) {
            var html = $('<option />').attr('value', t.pk).text('Target ' + t.value);
            $('select[name=aichi_targets]').append(html);
          });
          $('select[name=aichi_targets]').change();
          $('select[name=aichi_targets]').trigger("chosen:updated");
        })
      });
    }
  }).change();

  $('select[name=eu_targets]').on('change', function () {
    var text = $(this).parents('.form-group').find('.eu_target_text');
    var args = $("option:selected", this);
    var eu_actions = $('select[name=eu_actions]');
    var options = eu_actions.find('option:selected');
    var url = "{% url 'eu_target_title' pk=1%}";
    var action_url = "{% url 'target_action' pk=1%}";

    eu_actions.html('');
    text.html('');

    if (args.length == 0) {
      eu_actions.trigger('chosen:updated');
    }

    $.each(args, function(i, arg){
      $.get(url.replace('1', arg.value), function(data) {
        data = $.parseJSON(data)[0];
        text.append('<h5>Target '+ data.code + '</h5><p>' + data.value + '</p>');
      });

      $.get(action_url.replace('1', arg.value), function(data) {
        data = $.parseJSON(data);
        $.each(data, function (i, d) {
          var html = $('<option />').attr('value', d.id).text(d.value);
          var action_text =  eu_actions.parents('.form-group').find('.actions_text');

          action_text.html('');
          $.each(options, function(j, o) {
            if (o.value == d.id){
              html = $('<option />').attr('value', d.id).attr('selected', 'selected').text(d.value);
              $.get("{% url 'action_title' pk=1%}".replace('1', d.id), function(action_data) {
                action_data = $.parseJSON(action_data)[0];
                action_text.append('<h5>Action '+ action_data.code + ': '
                    + action_data.title + '</h5><p>' + action_data.value + '</p>');
              });
            }
          });
          eu_actions.append(html);
          eu_actions.trigger('chosen:updated');
        });
      });
    });
    eu_actions.change();
  }).change();
});
