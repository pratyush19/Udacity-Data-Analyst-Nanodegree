"""
Queries
"""

import csv, sqlite3

def number_of_nodes():
	result = cur.execute('SELECT COUNT(*) FROM nodes')
	return result.fetchone()[0]

def number_of_ways():
	result = cur.execute('SELECT COUNT(*) FROM ways')
	return result.fetchone()[0]

def number_of_unique_users():
	result = cur.execute('SELECT COUNT(DISTINCT(e.uid)) \
            FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways) e')
	return result.fetchone()[0]
    
def top_contributing_users():
	users = []
	for row in cur.execute('SELECT e.user, COUNT(*) as num \
            FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e \
            GROUP BY e.user \
            ORDER BY num DESC \
            LIMIT 10'):
		users.append(row)
	return users

def number_of_users_contributing_once():
	result = cur.execute('SELECT COUNT(*) \
            FROM \
                (SELECT e.user, COUNT(*) as num \
                 FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e \
                 GROUP BY e.user \
                 HAVING num=1) u')
	return result.fetchone()[0]

def common_ammenities():
	for row in cur.execute('SELECT value, COUNT(*) as num \
            FROM nodes_tags \
            WHERE key="amenity" \
            GROUP BY value \
            ORDER BY num DESC \
            LIMIT 10'):
		return row

def biggest_religion():
	for row in cur.execute('SELECT nodes_tags.value, COUNT(*) as num \
            FROM nodes_tags \
                JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value="place_of_worship") i \
                ON nodes_tags.id=i.id \
            WHERE nodes_tags.key="religion" \
            GROUP BY nodes_tags.value \
            ORDER BY num DESC \
            LIMIT 1;'):
		return row

def popular_cuisines():
	for row in cur.execute('SELECT nodes_tags.value, COUNT(*) as num \
            FROM nodes_tags \
                JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value="restaurant") i \
                ON nodes_tags.id=i.id \
            WHERE nodes_tags.key="cuisine" \
            GROUP BY nodes_tags.value \
            ORDER BY num DESC'):
		return row

if __name__ == '__main__':
	
	con = sqlite3.connect("/home/pk/ahmedabad.db")
	cur = con.cursor()
	
	print "Number of nodes: " , number_of_nodes()
	print "Number of ways: " , number_of_ways()
	print "Number of unique users: " , number_of_unique_users()
	print "Top contributing users: " , top_contributing_users()
	print "Number of users contributing once: " , number_of_users_contributing_once()
	print "Common ammenities: " , common_ammenities()
	print "Biggest religion: " , biggest_religion()
	print "Popular cuisines: " , popular_cuisines()
