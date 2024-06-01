
document.addEventListener('DOMContentLoaded', function () {
    var isEmployeeCheckbox = document.getElementById('id_is_employer');
    var employeeSkillsDiv = document.getElementById('employeeSkills');
    // var skillsSelect = document.getElementById('id_skills');
    var skillsSelect = document.querySelector('[name="skills"]');

    var addSkillButton = document.getElementById('addSkillButton');
    var selectedSkillsList = document.getElementById('selectedSkills');

    function updateSkillsField() {
          employeeSkillsDiv.style.display = isEmployeeCheckbox.checked ? 'none' : 'block';
        }

        isEmployeeCheckbox.addEventListener('change', function () {
          updateSkillsField();
        });

        // Initial check on page load
        updateSkillsField();

    addSkillButton.addEventListener('click', function () {
        var selectedSkill = skillsSelect.options[skillsSelect.selectedIndex];
        if (selectedSkill) {
            // Add the selected skill to the list
            var skillListItem = document.createElement('li');
            skillListItem.textContent = selectedSkill.text;
            selectedSkillsList.appendChild(skillListItem);

            // Remove the selected skill from the dropdown
            selectedSkill.remove();

            // Add a hidden input to include the selected skill in the form submission
            var hiddenInput = document.createElement('input');
            hiddenInput.type = 'hidden';
            hiddenInput.name = 'skills';
            hiddenInput.value = selectedSkill.value;
            document.getElementById('registrationForm').appendChild(hiddenInput);
        }
    });
});