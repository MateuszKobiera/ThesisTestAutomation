import json

from backend.Base_API_handler import BaseAPI


class MyPropertyAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.zone_instance = 'zone'
        self.zone_template = 'zonetemplate'

    def get_zone_templates(self) -> dict:
        """
        Return all zone templates as dict with name key
        :return:
        """
        zone_templates = self.send_request('get', self.zone_template)
        zone_templates_dict: dict = {}
        for zone_template in zone_templates:
            zone_templates_dict[zone_template['name']] = zone_template
        return zone_templates_dict
    
    def get_zone_instances(self) -> dict:
        """
        Return all zone templates as dict with name key
        :return:
        """
        zone_instances = self.send_request('get', self.zone_instance)
        zone_instances_dict: dict = {}
        for zone_instance in zone_instances:
            zone_instances_dict[zone_instance['name']] = zone_instance
        return zone_instances_dict

    def post_property(self, property_data: dict):
        """
        Create a new zone instance
        :return:
        """
        zone_templates = self.get_zone_templates()
        zone_instances = self.get_zone_instances()
        if 'structure' in property_data['tags'][0]:
            template_type = property_data['tags'][0].split(':')[2].capitalize()
            property_data['parentIds'] = zone_instances['Budynek']['id']
        elif 'building' in property_data['tags'][0]:
            template_type = property_data['tags'][0].split(':')[1].capitalize()
            property_data['parentIds'] = zone_instances['Sukiennice']['id']
        elif 'site' in property_data['tags'][0]:
            template_type = property_data['tags'][0].split(':')[1].capitalize()
        else:
            raise NameError('Check type of template na tags of property_data')
        property_data['templateId'] = zone_templates[template_type]['id']
        data = json.dumps(property_data)
        return self.send_request('post', self.zone_instance, data=data)

    def put_property(self, property_data: dict):
        """
        Update an existing zone instance
        :return:
        """
        zone_templates = self.get_zone_templates()
        property_data['templateId'] = zone_templates['Site']['id']
        zone_instances = self.get_zone_instances()
        zone_id = zone_instances[property_data['name']]['id']
        data = json.dumps(property_data)
        return self.send_request('put', self.zone_instance+f'/{zone_id}', data=data)
