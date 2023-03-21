const { Configuration, OpenAIApi } = require("openai");
const response = await openai.createCompletion({
    model: "code-davinci-002",
    prompt: "# Create a Python dictionary of 6 countries and their capitals\ncountries =",
    temperature: 0,
    max_tokens: 256,
    top_p: 1,
    frequency_penalty: 0,
    presence_penalty: 0,
});

const configuration = new Configuration({
     apiKey: "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"
});
const openai = new OpenAIApi(configuration);

