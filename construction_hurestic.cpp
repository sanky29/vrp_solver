#include<bits/stdc++.h>
using namespace std;

//so i am genrally working on the construction hurestic
/*
so int n: number of nodes
Q: capacity of vehicles
R: remaining vehicle
xkij matrix
distance matrix
demand
route vector with first entery as the remaining capacity
visited
*/


//the cost function  as
float cost (vector<vector<int> > ans, vector<vector<float> > dism){
float tc = 0.0;
 for(int i = 0 ; i < ans.size(); i++){
 	int prev = 0;
 	for(int j = 2 ; j < ans[i].size() ; j++){
 		tc = tc + dism[prev][ans[i][j]];
 		prev = ans[i][j];
	 }
 }
	 return (tc);
}

//update set of intial nodes
int update_set(vector<vector<float> > dism, vector<int>old_set, int o){
	
	float dis = 0.0;
	for(auto itr = old_set.begin(); itr != old_set.end(); itr++){
		float dis = 0.0;
		dis = pow(dism[o][*itr],.5) + dis;
	}
	int a = o;
		
	for(int i = 0; i < dism.size(); i++){
		
		float temp = 0.0;
		
		for(auto itr2 = old_set.begin(); itr2 != old_set.end(); itr2++){
			temp = temp + pow(dism[i][*itr2], .5);
		}
		
		if(temp > dis && find(old_set.begin(), old_set.end(), i) == old_set.end()){
			a = i;
			dis = temp;
		}
	}
	return a;
}

//generate k random number between 0,n
vector<int> random_numbers(int N , int K){
	srand(time(0)); 
	vector<int> n;
	vector<int> k;
	
	for(int i = 0; i < N ; i++){
		n.push_back(i);
		if(i < K){
			k.push_back(i);
		}
	}
	for(int i = 0; i < N; i++){
		int t = rand() % N;
		if( t < K){
			k[t] = n[i];
		}
	}
	return(k);
}

//construct solution 
vector< vector<int> > construct_solution(set<int> remained, vector<vector<int> > vehicles_remaining, vector< vector<float> > dism, vector< vector<int> > routes,
vector<int> d, int regret_depth) {
		while(not remained.empty()){
		
		//the best cost and the action
		vector<int> action;
		float regret = -1;
		
		for(auto it = remained.begin(); it != remained.end(); it++){
			
			//the k best actions
			set<float> cost_value;
			
			//vector<int> for best action till now
			vector<int> best_action;
			
			//check that we can directly add truck or not
			if(vehicles_remaining.size() > 0){
				best_action = {-1,*it,rand() % vehicles_remaining.size()};
				cost_value.insert(dism[*it][0]);
			}
			
			//now should work on routes as follows
			//now work for each route as
			for(int i = 0; i < routes.size(); i++){
			
				//check  whether this truck is possible or not
				if (routes[i][1] >= d[*it]){
					
					//go for each edge
					for(int j = 3; j < routes[i].size();j++){
						
						//the two cities are as follow
						int A = routes[i][j-1];
						int B = routes[i][j];
						
						//the increase in cost
						float c = dism[A][*it] + dism[*it][B] - dism[A][B];
						
						//check the cost value
						if(cost_value.size() < regret_depth){
							cost_value.insert(c);
							
							// if the insertion was best
							if(c <= *(cost_value.begin())){
								best_action = {i,*it,j};
							}
						}
						
						//check wether given action fits in possible actions
						else if(c < *(cost_value.rbegin())){
							
							//remove least one
							cost_value.erase(*(cost_value.begin()));
							
							//insert the c
							//check if best
							cost_value.insert(c);
							if(c <= *(cost_value.begin())){
								best_action = {i,*it,j};
							}
						}
					}
				}
			}
			//now check the action with other nodes
			//if best change value
			if(cost_value.size() > 0){
				if(regret <= *(cost_value.rbegin()) - *(cost_value.begin())){
					action = best_action;
					regret = *(cost_value.rbegin()) - *(cost_value.begin());
				}
			}
		}
			
		//---------------TAKE ACTION AS-----------------
		//check the action exist as
		if(action.size() > 0){
			
			//now check the action involve adding new route or not
			if(action[0] == -1){
				//add new route as
				routes.push_back({vehicles_remaining[action[2]][2],vehicles_remaining[action[2]][0] - d[action[1]], 0, action[1],0});
				
				//update the truck numbers as
				vehicles_remaining[action[2]][1]--;
				if(vehicles_remaining[action[2]][1] == 0){
					vehicles_remaining.erase(vehicles_remaining.begin() + action[2]);
				}
				
			}
			//now in other case we need to just add node
			else{
				routes[action[0]].insert(routes[action[0]].begin() + action[2], action[1]);
				routes[action[0]][1] = routes[action[0]][1] - d[action[1]];
			}
			//remove from remained points
			remained.erase(action[1]);
		}
	}
	return routes;
}

//remove sloution as
pair<set<int>, vector< vector<int> > > destroy_sol (vector<vector<float> >dis, vector< vector<int> > routes, float max_dis, vector<int> d){
	
	set<int> r;
	float radi = (static_cast <float> (rand()) / (static_cast <float> (RAND_MAX/max_dis)))/(2);
	int cn = rand()%(dis.size() - 1) + 1;
	cout <<"destroying solution: node: "<<cn <<"  radius:"<<radi<<endl;
	for(int i = 1 ; i < dis.size(); i++){
		if (dis[cn][i] < radi){
			r.insert(i);
		}
	}
	vector< vector<int>> ans = vector<vector<int> >(routes.size(), vector<int>());
	for (int i = 0; i < routes.size(); i++){
		ans[i].push_back(routes[i][0]);
		ans[i].push_back(routes[i][1]);
		ans[i].push_back(routes[i][2]);
		for(int j = 3; j < routes[i].size(); j++){
			if (r.end() == r.find(routes[i][j])){
				ans[i].push_back(routes[i][j]);
			}
			else{
				ans[i][1] = ans[i][1] + d[routes[i][j]];
			}
		}
	}
	return make_pair(r,ans);
}

//function responsible for calling constructor and destroyer
vector< vector<int> > construction_hurestic(int n, vector<float> x, vector<float> y,  vector<int> d, vector<int>veh_capa, vector<int>no_veh){	

	//route is search answer
	//ans is out best answer till now
	vector< vector<int> > routes;
	vector< vector<int> > ans;
	float max_capa = 0.0;
	float total_demand = 0.0;
	float max_dis = 0.0;
	
	//need to store this two things
	//the remaining type of vehicles and the remaining quantity
	vector<vector<int> > vehicles_remaining;
	for(int i = 0; i < veh_capa.size(); i++){
		vehicles_remaining.push_back({veh_capa[i], no_veh[i],i});
		max_capa = max(max_capa, (float)veh_capa[i]);
	}
	
	//the distant matrix
	vector<vector<float> > dism = vector<vector<float> >(n, vector<float>(n,0.0));
	
	//create distance matrix
	for(int i = 0 ; i< n ;i ++){
		total_demand = total_demand +  d[i];
		for(int j = 0 ; j < n ;j++){
			if(i < j){
				dism[i][j] = sqrt(pow(x[i]-x[j],2.0) + pow(y[i]-y[j],2.0));
				max_dis = max(dism[i][j], max_dis);
			}
			else{
				dism[i][j] = dism[j][i];
			}
		}
	}
	
	//-----------INTIALIZING ANSWER-------------------
	
	int start_route = (int)(total_demand/max_capa);
	//start with random 3 points
	vector<int> k = random_numbers(n,start_route);
	
	//the variable tracking the same output
	int same_output = 0;
	
	//the recursive updation of vector
	while(same_output < k.size()){
		int old_point = k.back();
		k.pop_back();
		int new_point = update_set(dism,k,old_point);
		if(new_point == old_point){
			same_output++;
		}
		else{
			same_output == 0;
		}
		k.insert(k.begin(),new_point);
	}
	
	int temp;
	for(int i = 0 ; i < k.size() ; i++){
		temp = rand() % no_veh.size();
		while(no_veh[temp] == 0){
			temp = rand() % vehicles_remaining.size();
		}
		vehicles_remaining[temp][1]--;
		routes.push_back({vehicles_remaining[temp][2],vehicles_remaining[temp][0],0,k[i],0});
		if(vehicles_remaining[temp][1] == 0){
			vehicles_remaining.erase(vehicles_remaining.begin() + temp);
		}
		
	}
	
	//---------------CHOSSING THE POINT---------------
	//choosing the regret depth as
	int regret_depth = n*(total_demand/max_capa);
	
	//we  need set of the all visited nodes
	set<int> remained;
	
	for(int i = 1; i < n; i++){
		remained.insert(i);
	}
	
	for(int i = 0; i < same_output; i++){
		remained.erase(k.back());
		k.pop_back();
	}
	
	routes = construct_solution(remained, vehicles_remaining,dism,routes,d,regret_depth);
	cout <<"solution intialized with cost "<<cost(routes,dism) <<endl;
	pair<set<int>, vector< vector<int> > > destroy = destroy_sol(dism,routes,max_dis,d);
	//routes = get<1>(destroy);
	
	//now work for each variable in remained set
	for(int tr = 0; tr < n*start_route; tr++) {
	pair<set<int>, vector< vector<int> > > destroy = destroy_sol(dism,routes,max_dis,d);
	vector<vector<int> > te = construct_solution(get<0>(destroy), vehicles_remaining,dism,get<1>(destroy),d,regret_depth);
	if( cost(te, dism) <= cost(routes, dism)){
		routes = te;
		cout <<"updating solution with cost "<<cost(routes,dism) <<endl;
	}
	}
	
	return routes;
	}

int main(){
 fstream x;
 x.open("graph.data");
 string s;
 x >> s;
 int n;
 x >> n;
 x >> s;
 int temp;
 x >> temp;
 vector<int> veh_capa = vector<int>(temp,0);
 vector<int> no_veh = vector<int>(temp,0);
 x>>s;
 for(int i = 0 ; i < temp ; i++){
 	x >> veh_capa[i];
 }
 x>>s;
 for(int i = 0 ; i < temp ; i++){
 	x >> no_veh[i];
 }
 x >> s;
 float xt,yt;
 cout << s << endl;
 vector<int> demand = vector<int>(n,0);
 vector<float> xc = vector<float>(n,0);
 vector<float> yc = vector<float>(n,0);
 for(int i = 0; i < n ; i++){
 	x >> xt;
 	x >> yt;
 	x >> demand[i];
 	xc[i] = (float)xt;
 	yc[i] = (float)yt;
 }
 vector< vector<int> > ans = construction_hurestic(n,xc,yc,demand,veh_capa,no_veh);
 	//the distant matrix
	vector<vector<float> > dism = vector<vector<float> >(n, vector<float>(n,0.0));
	
	//create distance matrix
	for(int i = 0 ; i< n ;i ++){
		for(int j = 0 ; j < n ;j++){
			if(i < j){
				dism[i][j] = sqrt(pow(xc[i]-xc[j],2.0) + pow(yc[i]-yc[j],2.0));
			}
			else{
				dism[i][j] = dism[j][i];
			}
		}
	}
 x.close();
 float tc = 0.0;
 ofstream myfile;
 myfile.open ("vrp.sol");
 for(int i = 0 ; i < ans.size(); i++){
 	int prev = 0;
 	myfile << "agent_";
 	myfile << ans[i][0];
 	myfile << " ";
 	for(int j = 2 ; j < ans[i].size() ; j++){
 		myfile << ans[i][j] << " ";
 		tc = tc + dism[prev][ans[i][j]];
 		prev = ans[i][j];
	 }
	 myfile << "\n";
 }
 cout << "TOTAL COST:  "<<tc <<endl;
}
