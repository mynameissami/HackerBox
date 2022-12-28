import configparser
config = configparser.ConfigParser()
config['DEFAULT'] = {'File-Type': 'Settings',
                 'Name': 'HackerBox',
                 'Description' : 'Settings File for HackerBox - Editable.',
				 'Warning' : 'Only Change this if you know what are you doing!'}
config['Main Settings'] = {
	'Auto-Update' : 'True',
	'Ask-For-Administrator' : 'True',
    'Auto-File-Sort' : 'True',
    
}
config['Commands Configuration'] = {
    'Custom-Youtube-Output-Directory' : 'Default',
    'Custom-Package-Download-Directory' : 'Default',
    'GitHub-Clone-Directory' : 'nil'
}

config['ScanFix Settings'] = {
    'Temp-Folder' : 'Default',
    'App-Data-Temp-Folder' : 'Default',
    'Windows-Temp-Folder' : 'Default',
}

with open('Settings.ini', 'w') as configfile:
    config.write(configfile)