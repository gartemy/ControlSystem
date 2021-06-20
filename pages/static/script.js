let $fileInput = $('.file-input');
let $droparea = $('.file-drop-area');
let $rulesOpen = $('.rules-open');
let $button = $('#update-btn');

// highlight drag area
$fileInput.on('dragenter focus click', function() {
  $droparea.addClass('is-active');
});

// back to normal state
$fileInput.on('dragleave blur drop', function() {
  $droparea.removeClass('is-active');
});

// change inner text
$fileInput.on('change', function() {
  let filesCount = $(this)[0].files.length;
  let $textContainer = $(this).prev();

  if (filesCount > 0) {
      $rulesOpen.hide();
      $button.show();
  }
  else {
      $button.hide();
      $rulesOpen.show();
  }

  if (filesCount === 1) {
    // if single file is selected, show file name
    let fileName = $(this).val().split('\\').pop();
    $textContainer.text(fileName);
  }
  else if (filesCount == 0) {
      $textContainer.text(' или перетащите их сюда')
  }
  else {
    // otherwise show number of files
    $textContainer.text(filesCount + ' документа выбрано');
  }
});