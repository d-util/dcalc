function goToVersion() {
    var version = document.getElementById("version-select").value;
    var currentPage = window.location.pathname.split('/').pop();
    window.location.href = "/docs/" + version + "/" + currentPage;
}
