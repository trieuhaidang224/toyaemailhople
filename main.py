#region import bailam_f
from s00_bailam import get_name_in_email as bailam_f
#endregion import bailam_f


#region chambai
from s02_chambai import chambai

#region testkey_list
testcase_list = [
  {'input': {'email_list':['ai-btx@gmail.com']                   }, 'output':['ai-btx']                                       , 'tc_name': 'tc0' }, 
  {'input': {'email_list':['user1@gmail.com', 'user2@gmail.com'] }, 'output':['user1', 'user2']                               , 'tc_name': 'tc1' }, 
  {'input': {'email_list':[]                                     }, 'output':[]                                               , 'tc_name': 'tc2' }, 
  {'input': {'email_list':['abb#ccc']                            }, 'output':['ERROR invaid email']                           , 'tc_name': 'tc3' }, 
  {'input': {'email_list':[None]                                 }, 'output':['ERROR invaid email']                           , 'tc_name': 'tc4' }, 
  {'input': {'email_list':[None, 'abb#ccc']                      }, 'output':['ERROR invaid email', 'ERROR invaid email']     , 'tc_name': 'tc5' }, 

  { 'input': [['im9']]                                                         , 'output': ['ERROR invaid email']                                            , 'tc_name': 'tc6', },
  { 'input': [['ortiznathan@example.net', 'brenthart@example.org']]            , 'output': ['ortiznathan', 'brenthart']                                      , 'tc_name': 'tc7', },
  { 'input': [['sabrina77@example.org']]                                       , 'output': ['sabrina77']                                                     , 'tc_name': 'tc8', },
  { 'input': [['lindsey85@example.com']]                                       , 'output': ['lindsey85']                                                     , 'tc_name': 'tc9', },
  { 'input': [['allennewman@example.org', None, 'jillsanders@example.com']]    , 'output': ['allennewman', 'ERROR invaid email', 'jillsanders']              , 'tc_name': 'tc10', },
  { 'input': [[]]                                                              , 'output': []                                                                , 'tc_name': 'tc11', },
  { 'input': [['er65#exampl', 'jordanlindsey@example.com']]                    , 'output': ['ERROR invaid email', 'jordanlindsey']                           , 'tc_name': 'tc12', },
  { 'input': [['lsantana@example.net', 'pmartin@example.net', None]]           , 'output': ['lsantana', 'pmartin', 'ERROR invaid email']                     , 'tc_name': 'tc13', },
  { 'input': [['mollymann@example.org']]                                       , 'output': ['mollymann']                                                     , 'tc_name': 'tc14', },
  { 'input': [[None, None, 'manningdavid@example.com']]                        , 'output': ['ERROR invaid email', 'ERROR invaid email', 'manningdavid']      , 'tc_name': 'tc15', },
]
#endregion testkey_list

ketqua_list = []
for tc in testcase_list:  # tc aka testcase
  INP_name = tc['input']
  tc_score, o_BAILAM = chambai(tc, bailam_f)

  ketqua_list.append({
    'tc_name'    : tc['tc_name'],
    'tc_score'   : tc_score,
    'o_TESTCASE' : tc['output'],
    'o_BAILAM'   : o_BAILAM,
  })
#endregion chambai

#region in ketqua
print('---ketqua chitiet')
for kq in ketqua_list:
  print(f'''
{kq['tc_name']} {kq['tc_score']}
o_TESTCASE = {kq['o_TESTCASE']}
o_BAILAM   = {kq['o_BAILAM']}
  '''.strip()+'\n')

print('\n---ketqua')
for kq in ketqua_list:
  print(f'''{kq['tc_name']} {kq['tc_score']}''')
#endregion in ketqua
