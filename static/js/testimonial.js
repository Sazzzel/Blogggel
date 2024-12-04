const editButtons = document.getElementsByClassName("btn-testimonial-edit");
const testimonialText = document.getElementById("id_body");
const testimonialForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
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
      let testimonialId = e.target.getAttribute("testimonial_id");
      deleteConfirm.href = `delete_testimonial/${testimonialId}`;
      deleteModal.show();
    });
  }
  

  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      let testimonialId = e.target.getAttribute("testimonial_id");
      deleteConfirm.href = `delete_testimonial/${testimonialId}`;
      deleteModal.show();
    });
  }