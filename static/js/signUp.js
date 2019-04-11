//This function is responsible for checking the given username is either in the database or not
//It shows a message to the user if username exists and prevent from submitting if username is taken
$(document).ready(function () {
	$('#signUpForm').on('submit', function (event) {
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