use druid::widget::{Align, Flex, Label, TextBox};
use druid::{AppLauncher, Data, Env, Lens, LocalizedString, Widget, WidgetExt, WindowDesc};

#[derive(Clone, Data, Lens)]
struct AppState {
    input_text: String,
    bubbles: Vec<String>,
}

fn main() {
    // Create the main window
    let main_window = WindowDesc::new(build_ui)
        .title(LocalizedString::new("Bubble App"))
        .window_size((400.0, 300.0));

    // Set up the initial state
    let initial_state = AppState {
        input_text: String::new(),
        bubbles: Vec::new(),
    };

    // Start the application
    AppLauncher::with_window(main_window)
        .use_simple_logger()
        .launch(initial_state)
        .expect("Failed to launch application");
}

fn build_ui() -> impl Widget<AppState> {
    // Create a Flex layout with a column orientation
    Flex::column()
        .cross_axis_alignment(druid::widget::CrossAxisAlignment::Start)
        .with_child(build_bubble_pane())
        .with_spacer(10.0)
        .with_child(build_input_box())
}

fn build_input_box() -> impl Widget<AppState> {
    // Create a TextBox for entering text
    TextBox::new()
        .controller(InputController)
        .on_activate(|ctx, data: &mut String, _: &Env| {
            // Move entered text to the bubbles pane
            ctx.submit_command(crate::commands::ADD_BUBBLE.with(data.clone()));
            data.clear();
        })
        .lens(AppState::input_text)
        .expand_width()
        .fix_height(30.0)
        .padding(5.0)
}

fn build_bubble_pane() -> impl Widget<AppState> {
    // Create a Flex layout with a column orientation for displaying bubbles
    Flex::column()
        .with_child(Label::new(|_, _| "Bubbles:").padding(5.0))
        .with_flex_child(
            Flex::column().with_child(build_bubble()).with_flex_child(Flex::column(), 1.0),
            1.0,
        )
}

fn build_bubble() -> impl Widget<AppState> {
    // Create a Label for displaying the bubbles
    Label::new(|data: &AppState, _: &Env| data.bubbles.join("\n")).padding(5.0)
}

struct InputController;

impl druid::widget::Controller<String, TextBox<AppState>> for InputController {
    fn event(
        &mut self,
        child: &mut TextBox<AppState>,
        ctx: &mut druid::EventCtx,
        event: &druid::Event,
        data: &mut String,
        env: &druid::Env,
    ) {
        child.event(ctx, event, data, env);

        // Handle custom command to add bubble
        if let druid::Event::Command(cmd) = event {
            if let Some(text) = cmd.get(crate::commands::ADD_BUBBLE) {
                // Add the entered text as a bubble
                data.push_str(&format!("\n{}", text));
                ctx.set_handled();
            }
        }
    }
}

mod commands {
    use druid::{Command, Selector};

    // Custom command to add a bubble
    pub const ADD_BUBBLE: Selector<String> = Selector::new("add-bubble");

    pub fn add_bubble<T: Into<String>>(text: T) -> Command {
        ADD_BUBBLE.with(text.into())
    }
}
