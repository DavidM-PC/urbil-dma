{
    'name': 'BIM purchase ext',

    'version': '14.0.0.0',

    'author': "Process Control",

    'contributors': ['Luis Felipe Paternina'],

    'website': "https://www.processcontrol.es/",

    'category': 'Quality',

    'depends': [

        'base',
        'purchase',
        'bim_project',
        'base_bim_2',

    ],

    'data': [
       
        'views/bim_project.xml',
        
    ],
    'installable': True
}
