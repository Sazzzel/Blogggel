/* jshint esversion: 6 */
const editButtons = document.getElementsByClassName("btn-testimonial-edit");
const testimonialText = document.getElementById("id_text");
const testimonialJob = document.getElementById("id_job_title");
const testimonialForm = document.getElementById("testimonialForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const addModal = new bootstrap.Modal(document.getElementById("addTestimonialModal"));
const deleteButtons = document.getElementsByClassName("btn-testimonial-delete");
const deleteConfirm = document.getElementById("deleteConfirm");



/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let testimonialId = e.target.getAttribute("data-testimonial-id");
      deleteConfirm.href = `delete_testimonial/${testimonialId}`;
      deleteModal.show();
    });
  }
  

  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      const testimonialId = e.target.getAttribute("data-testimonial-id");
      const content = document.getElementById(`testimonial-text${testimonialId}`).innerText;
      const job = document.getElementById(`testimonial-job${testimonialId}`).innerText;
      testimonialText.value = content;
      testimonialJob.value = job;
      submitButton.innerText = "Update";
      testimonialForm.setAttribute("action", `edit_testimonial/${testimonialId}/`);
      addModal.show();
    });
  }