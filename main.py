import datetime

# Basic setup for user data and AI state
user_profile = {
    "email": "dagracajoniel@gmail.com",
    "markets": {
        "crypto": {
            "fake_balance": 100,
            "estimates": {}
        },
        "stocks": {
            "fake_balance": 100,
            "estimates": {}
        },
        "forex": {
            "fake_balance": 100,
            "estimates": {}
        }
    }
}

def calculate_estimates(initial_amount, years):
    """
    Simulate long-term projections based on real AI learning. This is placeholder logic.
    """
    yearly_return_rate = 0.15  # 15% annual return as a learning simulation
    estimates = {}
    for year in range(1, years + 1):
        future_value = initial_amount * ((1 + yearly_return_rate) ** year)
        estimates[f"{year}_year"] = round(future_value, 2)
    return estimates

# Populate each market with estimates for 1 to 15 years
for market in user_profile["markets"]:
    initial = user_profile["markets"][market]["fake_balance"]
    user_profile["markets"][market]["estimates"] = calculate_estimates(initial, 15)

# Login system (placeholder for now)
def login(email):
    if email == user_profile["email"]:
        return f"Login successful for {email}"
    else:
        return "Login failed. Email not found."

# Dashboard (text-based for now)
def show_dashboard():
    print("===== AI Trading Bot Dashboard =====")
    print(f"User: {user_profile['email']}")
    for market, data in user_profile["markets"].items():
        print(f"\nMarket: {market.title()}")
        print(f"Fake Starting Balance: ${data['fake_balance']}")
        print("Profit Estimates:")
        for year, value in data["estimates"].items():
            print(f"  After {year.replace('_', ' ')}: ${value}")

# Run
print(login("dagracajoniel@gmail.com"))
show_dashboard()
