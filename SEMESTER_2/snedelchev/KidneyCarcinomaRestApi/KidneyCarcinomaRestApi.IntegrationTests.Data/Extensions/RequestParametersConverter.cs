namespace KidneyCarcinomaRestApi.IntegrationTests.Data.Extensions
{
    using System;
    using System.Linq;

    using Newtonsoft.Json.Linq;
    using Newtonsoft.Json;

    using KidneyCarcinomaRestApi.IntegrationTests.Data.ApiModels;
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Enums;

    public class RequestParametersConverter : JsonConverter
    {
        public override bool CanRead
        {
            get
            {
                return true;
            }
        }

        public override object ReadJson(
            JsonReader reader,
            Type objectType,
            object existingValue,
            JsonSerializer serializer)
        {
            var obj = (JObject)JObject.ReadFrom(reader);

            JProperty property = obj.Properties().FirstOrDefault();

            return new ApiRequestParameter(
                property.Name,
                property.Value.Value<string>(),
                ApiRequestParameterType.Body);
        }

        public override void WriteJson(
            JsonWriter writer,
            object value,
            JsonSerializer serializer)
        {
            ApiRequestParameter parameter = (ApiRequestParameter)value;

            JObject obj = new JObject();

            obj[parameter.Key] = parameter.Value;

            obj.WriteTo(writer);
        }

        public override bool CanConvert(Type t)
        {
            return typeof(ApiRequestParameter).IsAssignableFrom(t);
        }
    }
}
