import dns.resolver
import uuid
class Mimir:
    """Mimir is the figure renowned for his knowledge and wisdom."""
    def __init__(self, target):
        self.target = target

    def _txt(self):
        class TXT_Results:
            def __init__(self, value):
                self.id = uuid.uuid4()
                self.value = value
                self.tags = self._parse_tags()

            def _parse_tags(self):
                tags = {}
                if self.value:
                    parts = str(self.value).split(';')
                    for part in parts:
                        part = part.strip()
                        if '=' in part:
                            key, value = part.split('=', 1)
                            tags["key"] = key.strip()
                            tags["value"] = value.strip()
                return tags

            

        r_list: TXT_Results = []
        
        txt_results = dns.resolver.resolve(self.target, 'TXT')
        for value in txt_results:
            r_list.append(TXT_Results(value))
        
        return r_list
            


    def scan(self):
        txt_records = self._txt()
        for record in txt_records:
            print(f"\n{'='*60}")
            print(f"Record ID: {record.id}")
            print(f"{'-'*60}")
            print(f"Value:\n{record.value}")
            print(f"{'-'*60}")
            print(f"Parsed Data:")
            for key, value in record.tags.items():
                if isinstance(value, list):
                    print(f"  {key}:")
                    for item in value:
                        print(f"    - {item}")
                else:
                    print(f"  {key}: {value}")
            print(f"{'='*60}")