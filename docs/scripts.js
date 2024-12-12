// a js script for going to a version, to add compat
function goToVersion() {
    var version = document.getElementById("version-select").value;
    var currentPage = window.location.pathname.split('/').pop(); // Get the current file name
    window.location.href = "/docs/" + version + "/" + currentPage;
}
