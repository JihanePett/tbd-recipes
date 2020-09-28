function sendMail(contactForm) {
  emailjs
    .send("gmail", "studio_ghibli", {
      from_name: contactForm.name.value,
      from_email: contactForm.emailaddress,
      information_request: contactForm.projectsummary,
    })
    .then(
      function (response) {
        console.log("SUCCESS", response);
      },
      function (error) {
        console.log("FAILED", error);
      }
    );
  return false;
}