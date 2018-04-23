function check() {
    var dropdown = document.getElementById("propertyType");
    var current_value = dropdown.options[dropdown.selectedIndex].value;

    if (current_value == "garden") {
        document.getElementById("animalType").style.display = "block";
    }
    else {
        document.getElementById("OperationNos").style.display = "none";
    }
}