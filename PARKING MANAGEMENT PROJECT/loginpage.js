const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');
const viewPasswordButton = document.getElementById('viewPassword');
const passwordInput = document.getElementById('signinPassword');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});
viewPasswordButton.addEventListener('click', () => {
	if (passwordInput.type === 'password') {
		passwordInput.type = 'text';
			} else {
				passwordInput.type = 'password';
			}
		});
