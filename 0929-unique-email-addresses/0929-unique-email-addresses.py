class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def parse_email(email):
            result=''
            domain_idx=0
            plus_found=False
            for i in range(len(email)):
                if email[i]=='@':
                    domain_idx=i
                    break
                elif email[i]=='+':
                    plus_found=True
                elif email[i]!='.' and not plus_found:
                    result+=email[i]
            result+=email[domain_idx:]
            return result
        unique=set()
        for email in emails:
            email=parse_email(email)
            if email not in unique:
                unique.add(email)
        return len(unique)

                
                    

        