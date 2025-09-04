const slides = document.querySelectorAll(".slide");
let current = 0;

function showNextSlide() {
  slides[current].classList.remove("active");
  current = (current + 1) % slides.length;
  slides[current].classList.add("active");
}

setInterval(showNextSlide, 3000); // change every 3 sec

// Modal Logic
document.addEventListener('DOMContentLoaded', function() {
  const authModal = document.getElementById('authModal');
  const signInBtn = document.getElementById('signInBtn');
  const signUpBtn = document.getElementById('signUpBtn');
  const closeBtn = document.querySelector('.close-btn');
  const signInForm = document.getElementById('signInForm');
  const signUpForm = document.getElementById('signUpForm');
  const showSignUp = document.getElementById('showSignUp');
  const showSignIn = document.getElementById('showSignIn');

  // Open modal and show Sign In form
  signInBtn.onclick = function() {
    authModal.style.display = "block";
    signInForm.style.display = "block";
    signUpForm.style.display = "none";
  }

  // Open modal and show Sign Up form
  signUpBtn.onclick = function() {
    authModal.style.display = "block";
    signInForm.style.display = "none";
    signUpForm.style.display = "block";
  }

  // Close modal
  closeBtn.onclick = function() {
    authModal.style.display = "none";
  }

  // Close modal if user clicks outside of it
  window.onclick = function(event) {
    if (event.target == authModal) {
      authModal.style.display = "none";
    }
  }

});