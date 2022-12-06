from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import CovarianceShrinkage
from pypfopt.efficient_frontier import EfficientFrontier


df_compt = train[['date','close','tic']]
df_compt.set_index('date',inplace=True)
rest = df_compt.pivot(columns='tic', values='close')


mu = mean_historical_return(rest)
S = CovarianceShrinkage(rest).ledoit_wolf()

ef = EfficientFrontier(mu, S)
weights = ef.max_sharpe()

cleaned_weights = ef.clean_weights()
ef.save_weights_to_file("min_var_weights.txt")  # saves to file


weight_list = []
stock_list = []
for key, value in dict(cleaned_weights).items():
    stock_list.append(key)
    weight_list.append(value)
    


min_var_returns = (weight_list * ret_data)
min_var_returns.index= pd.to_datetime(weighted_returns.index)

min_var_distribution = pd.DataFrame({'Ativo': stock_list, 'Peso': weight_list})
min_var_distribution.set_index('Ativo',inplace= True)
min_var_distribution[min_var_distribution>0].dropna().plot(y = 'Peso', kind= 'pie', figsize =(20,20))

min_var_ptf= (min_var_returns.sum(axis=1,skipna=False))
min_var_ptf.name= 'Min Var PTF Returns'
min_var_ptf.index=DRL_strat.index