function selectOption() {
            var selectElement = document.getElementById("mySelect");
            var selectedOption = selectElement.options[selectElement.selectedIndex];
            selectedOption.selected = true
        }