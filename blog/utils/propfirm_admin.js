document.addEventListener("DOMContentLoaded", function () {
  const addAccountPlanButton = document.getElementById("add-account-plan");
  const accountPlansContainer = document.getElementById(
    "account-plans-container"
  );

  function addAccountPlan() {
    const newPlanDiv = document.createElement("div");
    newPlanDiv.classList.add("account-plan");
    newPlanDiv.innerHTML = `
            <input type="number" name="account_size" placeholder="Account Size" required>
            <input type="text" name="price" placeholder="Price" required>
            <input type="text" name="daily_drawdown" placeholder="Daily Drawdown">
            <input type="text" name="total_drawdown" placeholder="Total Drawdown">
            <button type="button" class="remove-account-plan">-</button>
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
