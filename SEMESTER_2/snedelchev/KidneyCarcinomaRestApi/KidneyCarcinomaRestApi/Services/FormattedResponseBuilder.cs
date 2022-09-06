namespace KidneyCarcinomaRestApi.Services
{
    using KidneyCarcinomaRestApi.Models.Responses;

    using Newtonsoft.Json;

    public class FormattedResponseBuilder
    {
        private static string jsonContentType = "application/json";

        public static FormattedResponse GetResponse(object response)
        {
            FormattedResponse result = new FormattedResponse()
            {
                ResponseString = BuildJsonResponse(response),
                ResponseType = jsonContentType
            }; 

            return result;
        }
        
        private static string BuildJsonResponse(object response)
        {
            return JsonConvert.SerializeObject(response);
        }
    }
}