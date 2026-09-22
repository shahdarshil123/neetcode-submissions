# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        domain_name = self.find_domain_name(startUrl)
        visit = set()
        visit.add(startUrl)

        result = [startUrl]
        def helper(input_url):
            urls = htmlParser.getUrls(input_url)

            for url in urls:
                if url in visit:
                    continue
                extracted_domain_name = self.find_domain_name(url)
                if extracted_domain_name == domain_name:
                    visit.add(url)
                    helper(url)
                    result.append(url)
        
        helper(startUrl)
        return result
        
    
    def find_domain_name(self, url) -> str:
        # find the domain name
        arr = []
        i = 7
        while i < len(url) and url[i] != '/':
            arr.append(url[i])
            i += 1
        
        domain = "".join(arr)
        return domain
    
    


            
