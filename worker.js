import configData from './config.json' assert { type: 'json' };

export default {
  async fetch(request) {
    const url = new URL(request.url);

    if (url.pathname === "/api/json") {
      return new Response(JSON.stringify(configData), {
        status: 200,
        headers: { "Content-Type": "application/json; charset=utf-8" }
      });
    }

    return new Response("Not Found", { status: 404 });
  }
};
