import json
result_data = []
with open('text_7.txt', encoding="utf-8") as f:
    companies_dict = {}
    profit_list = []
    bad_firm_dict = {}
    average_dict = {}
    for row in f:
        name, form, revenue, costs = row.split()
        profit = float(revenue) - float(costs)
        companies_dict[name] = profit

        if profit > 0:
            profit_list.append(profit)

    result_data.append(companies_dict)
    result_data.append({
        "average_profit": sum(profit_list) / len(profit_list)})

with open('result_task7.json', 'w', encoding="utf-8") as jsonfile:
    json.dump(result_data, jsonfile, ensure_ascii=False)