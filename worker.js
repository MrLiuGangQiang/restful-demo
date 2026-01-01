import configData from './config.json' assert { type: 'json' };

export default {
  async fetch(request) {
    return new Response(JSON.stringify(configData), {
      status: 200,
      headers: { "Content-Type": "application/json; charset=utf-8" }
    });
  }
};
