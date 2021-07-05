# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

perguntas = {
    1: "Aqui está a pergunta 1 - Verdadeiro ou Falso?",
    2: "Aqui é a pergunta 2 - Verdadeiro ou Falso?"
}

gabarito = {
    1: "Verdadeiro",
    2: "Falso"
}

retorno_respostas = {
    "Correta": "Muito bem, você acertou.",
    "Incorreta": "Que pena, você errou."
}

question_number = 0
acertos = 0

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Texto quando a skill for acionada."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class IniciarIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("IniciarIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global question_number, perguntas, acertos
        question_number = 1
        acertos = 0
        speak_output = "Agradeço por iniciar, aqui vai a primeira."
        speak_output += " " + perguntas[question_number]
        
        
        speak_output_2 = "Mensagem para caso demore em responder a primeira pergunta"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output_2)
                .response
        )

class VerdadeiroIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("VerdadeiroIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global question_number, perguntas, gabarito, acertos
        if gabarito[question_number] == "Verdadeiro":
            acertos += 1
            speak_output = retorno_respostas['Correta']
        else:
            speak_output = retorno_respostas['Incorreta']
        
        question_number += 1
        if question_number <= len(perguntas):
            speak_output += " Vamos para a próxima pergunta."
            speak_output += " " + perguntas[question_number]
        else:
            speak_output += f" Nossas perguntas acabaram. Você acertou {acertos} de {question_number-1} perguntas"
        
        speak_output_2 = "Mensagem para caso demore para dizer o próximo desafio."
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output_2)
                .response
        )

class FalsoIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FalsoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global question_number, perguntas, gabarito, acertos
        if gabarito[question_number] == "Falso":
            acertos += 1
            speak_output = retorno_respostas['Correta']

        else:
            speak_output = retorno_respostas['Incorreta']
        
        question_number += 1
        if question_number <= len(perguntas):
            speak_output += " Vamos para a próxima pergunta."
            speak_output += " " + perguntas[question_number]
        else:
            speak_output += f" Nossas perguntas acabaram. Você acertou {acertos} de {question_number-1} perguntas."
        
        speak_output_2 = "Mensagem para caso demore para dizer o próximo desafio."
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output_2)
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Você pode dizer 'Iniciar Quiz' para começarmos o desafio! Como posso ajudar?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Até mais!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, não entendi. Você pode dizer 'Iniciar Quiz' para começarmos o desafio."
        reprompt = "Eu não compreendi. Diga 'Iniciar Quiz' e, posteriormente, responda 'Verdadeiro' ou 'Falso'."

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Tive problemas em meu processamento. Por favor, tente novamente."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(IniciarIntentHandler())
sb.add_request_handler(VerdadeiroIntentHandler())
sb.add_request_handler(FalsoIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()