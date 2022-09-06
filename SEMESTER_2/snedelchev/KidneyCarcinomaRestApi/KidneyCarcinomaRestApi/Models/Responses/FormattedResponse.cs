namespace KidneyCarcinomaRestApi.Models.Responses
{
    public class FormattedResponse
    {
        public string ResponseString { get; set; }
        
        public string ResponseType { get; set; }

        public void Deconstruct(out string content, out string type)
        {
            content = this.ResponseString;
            type = this.ResponseType;
        }
    }
}