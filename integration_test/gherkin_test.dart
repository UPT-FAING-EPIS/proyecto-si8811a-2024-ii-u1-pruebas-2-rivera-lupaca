import 'package:flutter_gherkin/flutter_gherkin.dart';
import 'package:gherkin/gherkin.dart';
import 'package:test/test.dart';

Future<void> main() {
  final config = FlutterTestConfiguration()
    ..features = [RegExp(r'integration_test/features/*\.feature')]
    ..reporters = [
      ProgressReporter(),
      TestRunSummaryReporter(),
      JsonReporter(path: './report/report.json'), // Reporte en formato JSON
      HtmlReporter(path: './report/report.html'), // Reporte en formato HTML
    ]
    ..stepDefinitions = []
    ..restartAppBetweenScenarios = true
    ..targetAppPath = "test_driver/app.dart";

  return GherkinRunner().execute(config);
}
