$(document).ready(function() {
    $('#uploadForm').submit(function(event) {
        event.preventDefault();

        var formData = new FormData(this);

        var evtSource = new EventSource('/upload-status');
        var step = 0;

        evtSource.onmessage = function(event) {
            var status = event.data;
            step++;

            if (status.startsWith("/uploads/")) {
                var imgElement = $('#stepImage' + (step - 1));
                if (imgElement.length) {
                    imgElement.attr('src', status);
                }
            } else {
                var accordionItem = `
                    <div class="accordion-item">
                        <h2 class="accordion-header" id="heading${step}">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse${step}" aria-expanded="true" aria-controls="collapse${step}">
                                Step ${step}: ${status}
                            </button>
                        </h2>
                        <div id="collapse${step}" class="accordion-collapse collapse" aria-labelledby="heading${step}" data-bs-parent="#processAccordion">
                            <div class="accordion-body">
                                <p>${status}</p>
                                <img id="stepImage${step}" class="img-fluid" alt="Step ${step} image"/>
                            </div>
                        </div>
                    </div>`;
                $('#processAccordion').append(accordionItem);
            }
        };

        $.ajax({
            url: '/upload',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                evtSource.close();
                window.location.href = `/?processed_filename=${data.processed_filename}`;
            },
            error: function(xhr, status, error) {
                evtSource.close();
                $('#status').append('<p>Error during upload: ' + error + '</p>');
            }
        });
    });
});
