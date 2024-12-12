document.addEventListener("DOMContentLoaded", function () {
  const addAccountPlanButton = document.getElementById("add-account-plan");
  const accountPlansContainer = document.getElementById(
    "account-plans-container"
  );

  function addAccountPlan() {
    const newPlanDiv = document.createElement("div");
    newPlanDiv.classList.add("account-plan");
    newPlanDiv.innerHTML = `
  <div>
    <label>Phase</label>
    <select name="account_plans[]">
      <option value="one_phase">One Phase</option>
      <option value="two_phase">Two Phase</option>
      <option value="three_phase">Three Phase</option>
      <option value="four_phase">Four Phase</option>
      <option value="instant_funding">Instant Funding</option>
    </select>
  </div>
  <input type="number" name="account_size[]" placeholder="Account Size" required>
  <input type="text" name="price[]" placeholder="Price" required>
  <input type="text" name="profit_split_ratio[]" placeholder="Profit Split Ratio" required>
  <input type="text" name="daily_drawdown[]" placeholder="Daily Drawdown" required>
  <input type="text" name="total_drawdown[]" placeholder="Total Drawdown" required>
  <button type="button" class="remove-account-plan">Remove</button>
`;

    accountPlansContainer.appendChild(newPlanDiv);
  }

  addAccountPlanButton.addEventListener("click", addAccountPlan);

  // Remove account plan
  accountPlansContainer.addEventListener("click", function (e) {
    if (e.target.classList.contains("remove-account-plan")) {
      e.target.parentElement.remove();
    }
  });
});
