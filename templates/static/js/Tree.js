var j=0;
var str=""	
var id=""
	
$(document).ready(
		function() {

			$(function() {
				$('.tree li').addClass('parent_li').find(' > span').attr(
						'title', 'Collapse this branch');
				$('.tree li.parent_li > span').on(
						'click',
						function(e) {
							var children = $(this).parent('li.parent_li').find(
									' > ul > li');
							if (children.is(":visible")) {
								children.hide('fast');
								$(this).attr('title', 'Expand this branch')
										.find(' > i').addClass('icon-plus-sign')
										.removeClass('icon-minus-sign');
							} else {
								children.show('fast');
								$(this).attr('title', 'Collapse this branch').find(
										' > i').addClass('icon-minus-sign')
										.removeClass('icon-plus-sign');
							}
							e.stopPropagation();
						});
				$('.tree li.parent_li > span').on('click', function (e) {
			    	j=0
			    	id=""
			    	str=""
			        id=$(this).attr('id');
			        
			    	nt=0
			    	while(j<id.length && id[j]!='.' ){
			    		nt=nt*10+parseInt(id[j]);
			    		j++
			    		
			    	}
			    	j++
			    	
			    	//filling editor
			    	var to=id_to_path(id,obj,str) 
			    	
			    	
			    	var params = {
			    	    path: to,
			    	 };
			    	
			    	var editor_text=""
			    	console.log(to);
			    	$.post("/rmi_servlet/FileServlet", $.param(params), function(response) {
			    	    editor_text=String(response)

			    	    var editor = ace.edit("editor");
			    	    
			    	    editor.setTheme("ace/theme/xcode");
			    	    editor.getSession().setMode("ace/mode/javascript");
			    	    
			    	    editor.setValue(editor_text)
			    	});
			        
			        
			    	//console.log(obj)
			    });
				
//				
//				$("#download_file").on('click', function (e) {
//					var path = document.getElementById("myText").value
//					console.log("path="+path)
//			    	var params = {
//			    	    path: path,
//			    	 };
//			    	
//			    	$.post("/rmi_servlet/login.do", $.param(params), function(response) {
//			    		alert("downloaded")
//			    	});
//			        
//			        
//			    	//console.log(obj)
//			    });
				
				
				
			    
		}); 
			
			var json = $('#current_div').val();

			var obj = JSON.parse(json);
			$('.tree').append(input(obj, 0, ""));

			
			$("#horizontal").kendoSplitter({
				panes : [ {
					collapsible : true,
					collapsible : true,
				}, ]
			});


			
			///////////////////
						
			/////////////
			

		});

function input(obj, level, str) {

	if (obj.type === "directory") {
		var ul = $('<ul/>');
		str += level + "."
		var li = $('<li/>').appendTo(ul);
		var t = $('<span id=' + str + ' />').append(
				$('<i/>').addClass('icon-minus-sign'));
		t.append(obj.name);
		t.append()

		li.append(t);
		$.each(obj.subDir, function(i) {

			li.append(input(obj.subDir[i], i, str))

		});
		return ul;
	} else if (obj.type === "file") {
		var ul = $('<ul/>');
		str += level + "."
		var li = $('<li/>').appendTo(ul);
		var t = $('<span id=' + str + ' />').append(
				$('<i/>').addClass('icon-leaf'));
		t.append(obj.name);

		li.append(t);
		return ul;
	}

}

function id_to_path(id, obj, str) {
	var nt = 0;

	while (j < id.length && id[j] != '.') {
		nt = nt * 10 + parseInt(id[j]);
		j++
	}
	j++
	// console.log(j)

	str = obj.name + '/'

	if (obj.type === "directory") {

		str += id_to_path(id, obj.subDir[nt], str)

	}
	return str

}
