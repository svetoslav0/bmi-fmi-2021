namespace KidneyCarcinomaRestApi.Helpers
{
    using System.Linq;
    using System.Text;

    public static class StringUtils
    {
        public static string ToSnakeCase(this string str)
        {
            return string.Concat(str.Select((x, i) => i > 0 && char.IsUpper(x) ? "_" + x.ToString() : x.ToString())).ToLower();
        }
        
        public static string ToUpperCamelCase(this string str)
        {
            char[] characters = str.ToCharArray();
            StringBuilder wordBuilder = new StringBuilder();
            
            for (int currentIndex = 0; currentIndex < characters.Length; currentIndex++)
            {
                if (currentIndex == 0)
                {
                    wordBuilder.Append(characters[currentIndex]);
                }
                else if (characters[currentIndex] == '_')
                {
                    wordBuilder.Append(char.ToUpper(characters[currentIndex + 1]));
                    currentIndex++;
                }
            }

            return wordBuilder.ToString();
        }
    }
}