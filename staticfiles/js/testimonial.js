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
  
/**
* Initializes edit functionality for the provided edit buttons.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    // Get the ID
    const testimonialId = e.target.getAttribute("data-testimonial-id");
    // Get the text
    const content = document.getElementById(`testimonial-text${testimonialId}`).innerText;
    // get the role
    const job = document.getElementById(`testimonial-job${testimonialId}`).innerText;
    // update the add form with the data
    testimonialText.value = content;
    testimonialJob.value = job;
    // Change its functionality Edit
    submitButton.innerText = "Update";
    testimonialForm.setAttribute("action", `edit_testimonial/${testimonialId}/`);

    // Show the modal that contains the form.
    addModal.show();
  });
}