(function ($) {

	$(document).ready(function() {
		var curname = $('#id_name').val();
		
		$.addMultiselect = function(in_persons, in_classname, in_labelid, in_labelname, in_listselected) {
			var local_listselect = [];
			local_listselect.push('<div class="form-row ' + in_classname + '"><div><label for="' + in_labelid + '" class="required">' + in_labelname + ':</label><select  multiple="multiple" id="select' + in_classname + '">');
			
			var selected = '';
			for (person in in_persons) {
				if (in_persons[person].name != curname) {
					if (in_listselected.indexOf(in_persons[person].id) >= 0) {selected = 'selected="selected"'} else { selected = '' }
					local_listselect.push('<option ' + selected +  ' id="' + in_persons[person].id + '">' + in_persons[person].name + '</option>');					
				}
			}
			local_listselect.push('</select></div></div>');
			$('fieldset.module').append(local_listselect.join(''));	
		}
		
		$.selectToStr = function(in_classname, in_idtextarea) {
			var local_listselected = [];
			$('#select' + in_classname + ' option:selected').each(function() {local_listselected.push($(this).attr('id'))});
			$('#' + in_idtextarea).val(local_listselected.join(' '));
		}
		
		$.getJSON( "/folowers/", { name: curname }, function(json) {
			persons = json[0]
			pursued = json[1];
			pursuers = json[2];
			
			$.addMultiselect(persons, 'pursued', 'id_pursuedms', 'Преследуемые', pursued);
			$.addMultiselect(persons, 'pursuers', 'id_pursuersms', 'Преследователи', pursuers);
		});
		
		$('.submit-row input[type="submit"]').click(function() {

			$.selectToStr('pursued', 'id_follow_ids');
			$.selectToStr('pursuers', 'id_pursuers');

			//var pursuers_list = [];
			//$('#pursuers>option:selected').each(function() {pursuers_list.push($(this).attr('id'))});
			//$('#id_pursuers').val(pursuers_list.join(' '));
			
			return true;
		});
			
	});
})(django.jQuery);

