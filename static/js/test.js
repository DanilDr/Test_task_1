(function ($) {
	$(document).ready(function() {
		var curname = $('#id_name').val();
		$.getJSON('/folowers/', {}, 
			function(data) {
				var listfolowerms = ['<select class="selectfolower"  multiple="multiple">',];
				var listfolower = $('#id_follow_ids').val().split(' ');
				for (folower in data) {
					if (curname != data[folower].name) {
						var select = (listfolower.indexOf(data[folower].id.toString()) >= 0 ? ' selected="selected" ' : '');
						listfolowerms.push('<option ' + select +  ' value="' + data[folower].id + '">' + data[folower].name + '</option>');
					}
				};
				listfolowerms.push('</select>');
				$('#id_follow_ids').hide();
				$('.field-follow_ids>div').append(listfolowerms.join(''));
			}
		);
		$('.submit-row>input[type="submit"]').click(function() {
			var listfolower = []
			$('.selectfolower>option:selected').each(function() {
				listfolower.push($(this).attr('value'));
			});
			$('#id_follow_ids').val(listfolower.join(' '));
			$.get('/initdb/', {'name' : curname}, function(data) {});
			return true;
		});
	});
})(django.jQuery);

