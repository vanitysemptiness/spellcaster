// controllers.rs
use serde_json::Value;

pub fn hello_handler(name: String) -> impl warp::Reply {
    warp::reply::html(format!("Hello, {}!", name))
}

pub fn post_handler(body: Value) -> impl warp::Reply {
    // Process the JSON body as needed
    println!("Received JSON: {:?}", body);
    warp::reply::json(&body)
}