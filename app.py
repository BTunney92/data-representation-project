from flask import Flask, url_for, request, jsonify, abort

#from IPython.display import YouTubeVideo

from votedao import voteDAO

app = Flask(__name__, static_url_path='', static_folder='static')

goals = [
    {'name':'Zinedine Zidane Vs Italy (2006))'}, 
    {'name':'Siphiwe Tshabalala Vs Mexico (2010)'},
	{'name':'Maxi Rodriguez Vs Mexico (2006)'},
    {'name':'Robin Van Persie Vs Spain (2014)'},
	{'name':'Diego Maradona Vs England (1986)'},
]


@app.route('/goal', methods=['GET'])
def getAllgoals():
    return jsonify(goals)

@app.route('/vote/<goalname>', methods=['POST'])

def voteForGoal(goalname):
    ip_addr = request.remote_addr
    data = (goalname, ip_addr)
    newid = voteDAO.create(data)

    return jsonify({'id':newid})

@app.route('/vote/<goalname>', methods=['GET'])
def getCountForgoal(goalname):
    count = voteDAO.countvotes(goalname)
    return jsonify({goalname:count})

@app.route('/vote', methods=['GET'])
def getAllCount():
    allcounts = []
    for goal in goals:
        goalname = goal['name']
        count = voteDAO.countvotes(goalname)
        allcounts.append({goalname:count})
        
    return jsonify(allcounts)

@app.route('/vote/all', methods=['delete'])
def deleteAllVote():
    return jsonify({'done':True})

if __name__ == "__main__":
    app.run(debug=True)
   
    
    
    
    