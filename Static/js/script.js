document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM fully loaded and parsed");  // Check if DOM is fully loaded
    var currentScenarioIndex = 1;
    var totalScenarios = document.querySelectorAll('.scenario-container').length;

    console.log("Total scenarios: ", totalScenarios);  // Log the total number of scenarios

    function showScenario(index) {
        console.log("Attempting to show scenario index: ", index);  // Debug log to see which index is being attempted to show
        document.querySelectorAll('.scenario-container').forEach((scenario, i) => {
            if (i + 1 === index) {
                console.log("Displaying scenario number: ", i + 1);  // Confirm which scenario is being displayed
                scenario.style.display = 'block';
            } else {
                scenario.style.display = 'none';
            }
        });
        currentScenarioIndex = index;
        console.log("Current scenario index set to: ", currentScenarioIndex);  // Log the current scenario index after change
    }

    function nextScenario() {
        console.log("Next button clicked, current index before increment: ", currentScenarioIndex);  // Log before changing scenario
        if (currentScenarioIndex < totalScenarios) {
            showScenario(currentScenarioIndex + 1);
        } else {
            console.log("Attempted to exceed total scenario count.");  // Log if trying to go beyond available scenarios
        }
    }

    function prevScenario() {
        console.log("Prev button clicked, current index before decrement: ", currentScenarioIndex);  // Log before changing scenario
        if (currentScenarioIndex > 1) {
            showScenario(currentScenarioIndex - 1);
        } else {
            console.log("Already at the first scenario.");  // Log if trying to go below the first scenario
        }
    }

    var prevButton = document.getElementById('prevButton');
    var nextButton = document.getElementById('nextButton');

    if (!prevButton || !nextButton) {
        console.error('Navigation buttons not found. Check your HTML to ensure they exist with the correct IDs.');  // Error log if buttons not found
    } else {
        prevButton.addEventListener('click', prevScenario);
        nextButton.addEventListener('click', nextScenario);
    }

    showScenario(currentScenarioIndex);  // Initialize by showing the first scenario
});

// Function to display a warning alert if the wrong button ("Yes") is clicked
function showWrongButtonAlert() {
    alert("You've clicked the wrong button. Please select the other button to proceed.");
}
