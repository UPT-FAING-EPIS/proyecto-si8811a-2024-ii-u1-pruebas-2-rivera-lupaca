import 'package:flutter_gherkin/flutter_gherkin.dart';
import 'package:gherkin/gherkin.dart';

StepDefinitionGeneric GivenIAmOnTheLoginScreen() {
  return given<FlutterWorld>(
    'I am on the login screen',
    (context) async {
      await context.world.appDriver.waitForAppToSettle();
    },
  );
}

StepDefinitionGeneric ThenIExpectButtonToBePresent() {
  return then<FlutterWorld>(
    'I expect the {string} button to be present',
    (context, buttonName) async {
      await context.world.appDriver.waitFor(find.byValueKey(buttonName), timeout: Duration(seconds: 5));
    },
  );
}

StepDefinitionGeneric WhenITapTheButton() {
  return when<FlutterWorld>(
    'I tap the {string} button',
    (context, buttonName) async {
      await context.world.appDriver.tap(find.byValueKey(buttonName));
    },
  );
}

StepDefinitionGeneric ThenIExpectToSeeMessage() {
  return then<FlutterWorld>(
    'I expect to see a confirmation message {string}',
    (context, message) async {
    },
  );
}

List<StepDefinitionGeneric> loginSteps() {
  return [
    GivenIAmOnTheLoginScreen(),
    ThenIExpectButtonToBePresent(),
    WhenITapTheButton(),
    ThenIExpectToSeeMessage(),
  ];
}
