from collections import defaultdict


def solution(order):

    table = {}
    menu = []
    for i in order:

        if i[2] not in menu:
            menu.append(i[2])
        if i[1] not in table:
            table[i[1]] = {}

        if i[2] not in table[i[1]]:
            table[i[1]][i[2]] = 1
        else:
            table[i[1]][i[2]] += 1

    print(menu)
    print(table)
    menu = sorted(menu)
    menu.insert(0, 'Tables')
    print(menu)
    table = sorted(table.items(), key=lambda x: int(x[0]))
    print(table)

    result = []
    result.append(menu)

    for k, v in table:
        info = [k]
        for food in menu[1:]:
            if food not in v:
                info.append('0')
            else:
                info.append(str(v[food]))

        result.append(info)

    print(*result, sep="\n")
    return result


def newSolution(orders):
    menu = set()
    tableOrder = {}
    for _, table, order in orders:
        menu.add(order)
        if table not in tableOrder:
            tableOrder[table] = {}
        tableOrder[table][order] = tableOrder[table].get(order, 0) + 1

    result = [["Table"] + sorted(menu)]
    for table in sorted(tableOrder.keys(), key=lambda x: int(x)):
        order = tableOrder[table]
        row = [table]
        for dish in result[0][1:]:
            row.append(str(order.get(dish, 0)))
        result.append(row)
    return result
#=====•======#


o1 = [["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"], [
    "Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]
o2 = [["James", "12", "Fried Chicken"], ["Ratesh", "12", "Fried Chicken"], ["Amadeus", "12",
                                                                            "Fried Chicken"], ["Adam", "1", "Canadian Waffles"], ["Brianna", "1", "Canadian Waffles"]]
o3 = [["Laura", "2", "Bean Burrito"], [
    "Jhon", "2", "Beef Burrito"], ["Melissa", "2", "Soda"]]

print(solution(o1))
print(solution(o2))
print(solution(o3))

print(newSolution(o1))
print(newSolution(o2))
print(newSolution(o3))
