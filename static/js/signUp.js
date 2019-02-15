$(document).ready(function() {
	$('#signUpForm').on('submit', function(event) {
		$.ajax({
			data : {
				username : $('#inputUsername').val(),
				email : $('#inputEmail').val()
			},
			type : 'POST',
			url : '/sign_up'
		})
		.done(function(exist) {
			if (exist == "username_exists"){
				$('#usernameErrorAlert').show();
				$('#emailErrorAlert').hide();
			}
			else if(exist == "email_exists") {
				$('#emailErrorAlert').show();
				$('#usernameErrorAlert').hide();
			}
			else if(exist == "email_and_username_exist") {
				$('#emailErrorAlert').show();
				$('#usernameErrorAlert').show();
			}
			else{
				$('#usernameErrorAlert').hide();
				$('#emailErrorAlert').hide();
				window.location.reload(); 
			}
		});
		event.preventDefault();
	});

});