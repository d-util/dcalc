function goToVersion() {
    var version = document.getElementById("version-select").value;
    var currentPage = window.location.pathname.split('/').pop(); // Get the current file name
    window.location.href = "/dcalc/" + version + "/" + currentPage;
}
