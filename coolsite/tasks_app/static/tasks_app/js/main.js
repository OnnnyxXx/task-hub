document.addEventListener('DOMContentLoaded', function() {
    var checkbox = document.getElementById('side-checkbox');
    var panel = document.querySelector('.side-panel');

    checkbox.addEventListener('change', function() {
        if (checkbox.checked) {
            document.addEventListener('click', closePanel);
        } else {
            document.removeEventListener('click', closePanel);
        }
    });

    function closePanel(event) {
        var toggleButton = document.querySelector('.side-button-1, .side-button-2');
        if (!panel.contains(event.target) && !toggleButton.contains(event.target)) {
            checkbox.checked = false;
        }
    }
});